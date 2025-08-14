document.addEventListener("DOMContentLoaded", function () {

    function setViewMode() {
        document.getElementById('firstName').readOnly = true;
        document.getElementById('lastName').readOnly = true;
        document.getElementById('program').disabled = true;
        document.getElementById('gender').disabled = true;
        document.getElementById('year').readOnly = true;

        document.getElementById('doneButton').style.display = 'none';
        document.getElementById('cancelstud').style.display = 'none';
        document.getElementById('updateimage').style.display = 'none';
        document.getElementById('modalDeleteButton').style.display = 'none';

        document.getElementById('modalEditButton').style.display = 'block';
        document.getElementById('searchStudentModalLabel').textContent = 'Student Information';
    }

    function setEditMode() {
        document.getElementById('firstName').readOnly = false;
        document.getElementById('lastName').readOnly = false;
        document.getElementById('program').disabled = false;
        document.getElementById('gender').disabled = false;
        document.getElementById('year').readOnly = false;

        document.getElementById('doneButton').style.display = 'block';
        document.getElementById('cancelstud').style.display = 'block';
        document.getElementById('updateimage').style.display = 'block';
        document.getElementById('modalDeleteButton').style.display = 'block';

        document.getElementById('modalEditButton').style.display = 'none';
        document.getElementById('searchStudentModalLabel').textContent = 'Edit Student Information';
        document.getElementById('doneButton').textContent = 'SAVE';
        document.getElementById('addStudentForm').action = '/edit/' + document.getElementById('studentID').value;
    }

    function confirmDelete(studentID) {
        if (confirm('Are you sure you want to delete this student?')) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/delete/${studentID}`;
            const hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = 'csrf_token';
            hiddenInput.value = '{{ csrf_token() }}';
            form.appendChild(hiddenInput);
            document.body.appendChild(form);
            form.submit();
        }
    }

    // Event delegation for table buttons
    document.querySelector("table tbody").addEventListener("click", function (e) {
        const button = e.target.closest("button");
        if (!button) return;

        const studentId = button.dataset.id;

        if (button.classList.contains("show-details-btn") || button.classList.contains("edit-btn")) {
            fetch(`/student?query=${encodeURIComponent(studentId)}`)
                .then(res => res.json())
                .then(data => {
                    if (!data) return;
                    document.getElementById("studentID").value = data.id;
                    document.getElementById("firstName").value = data.firstname;
                    document.getElementById("lastName").value = data.lastname;
                    document.getElementById("program").value = data.program_code;
                    document.getElementById("gender").value = data.gender;
                    document.getElementById("year").value = data.year;
                    document.getElementById("studentImage").src = data.image_url !== "NO_IMAGE"
                        ? data.image_url
                        : "https://via.placeholder.com/150";

                    if (button.classList.contains("show-details-btn")) {
                        setViewMode();
                        $('#searchStudentModal').modal('show');
                    } else {
                        setEditMode();
                        $('#searchStudentModal').modal('show');
                    }
                });
        } 
        else if (button.classList.contains("del-btn")) {
            confirmDelete(studentId);
        }
    });

    // Modal buttons
    document.getElementById('modalEditButton').addEventListener('click', setEditMode);
    document.getElementById('cancelstud').addEventListener('click', setViewMode);
    document.getElementById('closebutton').addEventListener('click', setViewMode);
    document.getElementById('modalDeleteButton').addEventListener('click', function () {
        confirmDelete(document.getElementById('studentID').value);
    });

    // Search button
    document.getElementById("searchButton").addEventListener("click", function () {
        const query = document.getElementById("studentSearch").value.trim();
        if (!query) return;

        fetch(`/search_students?query=${encodeURIComponent(query)}`)
            .then(res => res.json())
            .then(data => {
                const tbody = document.querySelector("table tbody");
                tbody.innerHTML = "";

                if (data.length === 0) {
                    tbody.innerHTML = `<tr><td colspan="8" class="text-center">No matching students found</td></tr>`;
                    return;
                }

                data.forEach(student => {
                    tbody.innerHTML += `
                        <tr>
                            <td><img src="${student.image_url}" style="width:50px; height:50px; border-radius:50%; background-color:#555;"></td>
                            <td>${student.firstname}</td>
                            <td>${student.lastname}</td>
                            <td>${student.id}</td>
                            <td>${student.program_code}</td>
                            <td>${student.gender}</td>
                            <td>${student.year}</td>
                            <td>
                                <button type="button" class="btn btn-info btn-sm show-details-btn" style="border-color: black; background-color: white;" data-id="${student.id}">Show Details</button>
                                <button type="button" class="btn btn-secondary btn-sm edit-btn" data-id="${student.id}">Edit</button>
                                <button type="button" class="btn btn-sm del-btn" data-id="${student.id}" style="border-color:red;background-color:transparent;color:red;">Delete</button>
                            </td>
                        </tr>
                    `;
                });
            });
    });
});
