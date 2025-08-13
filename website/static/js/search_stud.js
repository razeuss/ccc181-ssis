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

    function bindTableButtons() {
        document.querySelectorAll(".show-details-btn, .edit-btn, .del-btn").forEach(button => {
            button.addEventListener("click", function () {
                const studentId = this.dataset.id;
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

                        if (this.classList.contains("show-details-btn")) {
                            setViewMode();
                            $('#searchStudentModal').modal('show');
                        } else if (this.classList.contains("edit-btn")) {
                            setEditMode();
                            $('#searchStudentModal').modal('show');
                        } else if (this.classList.contains("del-btn")) {
                            confirmDelete(data.id);
                        }
                    });
            });
        });
    }

    bindTableButtons();

    // Modal edit button
    document.getElementById('modalEditButton').addEventListener('click', setEditMode);

    // Cancel inside modal
    document.getElementById('cancelstud').addEventListener('click', setViewMode);

    // Close inside modal
    document.getElementById('closebutton').addEventListener('click', setViewMode);

    // Delete inside modal
    document.getElementById('modalDeleteButton').addEventListener('click', function () {
        confirmDelete(document.getElementById('studentID').value);
    });
});
