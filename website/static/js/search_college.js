// Search button click
document.getElementById('searchCollegeBtn').addEventListener('click', function () {
    const query = document.getElementById('collegeinput').value;

    fetch(`/search_college?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("table tbody");
            tbody.innerHTML = ""; // Clear current rows

            if (data.length > 0) {
                data.forEach(college => {
                    const tr = document.createElement("tr");

                    tr.innerHTML = `
                        <td>${college.code}</td>
                        <td>${college.name}</td>
                        <td>
                            <button type="button" class="btn btn-info btn-sm show-details" data-id="${college.code}" style="border-color: black; background-color: white;">Show Details</button>
                            <button type="button" class="btn btn-secondary btn-sm edit-college" data-id="${college.code}">Edit</button>
                            <button type="button" class="btn btn-sm delete-college" data-id="${college.code}" style="border-color: red; background-color: transparent; color: red;">Delete</button>
                        </td>
                    `;
                    tbody.appendChild(tr);
                });

                bindActionButtons();
            } else {
                tbody.innerHTML = `<tr><td colspan="3" class="text-center">No results found</td></tr>`;
            }
        })
        .catch(err => console.error(err));
});

// Bind Show Details / Edit / Delete buttons
function bindActionButtons() {
    // Show Details
    document.querySelectorAll(".show-details").forEach(btn => {
        btn.addEventListener("click", function () {
            const collegeCode = this.dataset.id;
            fetch(`/search_college?query=${encodeURIComponent(collegeCode)}`)
                .then(res => res.json())
                .then(data => {
                    if (data.length > 0) {
                        const col = data[0];
                        document.getElementById('collegeCode').value = col.code;
                        document.getElementById('collegeName').value = col.name;
                        document.getElementById('collegeCode').readOnly = true;
                        document.getElementById('collegeName').readOnly = true;
                        document.getElementById('donecollege').style.display = 'none';
                        document.getElementById('deletecollege').style.display = 'none';
                        document.getElementById('cancelcollege').style.display = 'none';
                        document.getElementById('editcollege').style.display = 'block';
                        document.getElementById('searchcollegelabel').textContent = 'College Information';
                        $('#searchcollege').modal('show');
                    }
                });
        });
    });

    // Edit College
    document.querySelectorAll(".edit-college").forEach(btn => {
        btn.addEventListener("click", function () {
            const collegeCode = this.dataset.id;
            fetch(`/search_college?query=${encodeURIComponent(collegeCode)}`)
                .then(res => res.json())
                .then(data => {
                    if (data.length > 0) {
                        const col = data[0];
                        document.getElementById('collegeCode').value = col.code;
                        document.getElementById('collegeName').value = col.name;
                        document.getElementById('collegeCode').readOnly = false;
                        document.getElementById('collegeName').readOnly = false;
                        document.getElementById('donecollege').style.display = 'block';
                        document.getElementById('deletecollege').style.display = 'block';
                        document.getElementById('cancelcollege').style.display = 'block';
                        document.getElementById('editcollege').style.display = 'none';
                        document.getElementById('searchcollegelabel').textContent = 'Edit College Information';
                        document.getElementById('addcollegeForm').action = '/updatecollege/' + col.code;
                        document.getElementById('donecollege').textContent = 'SAVE';
                        $('#searchcollege').modal('show');
                    }
                });
        });
    });

    // Delete College
    document.querySelectorAll(".delete-college").forEach(btn => {
        btn.addEventListener("click", function () {
            const collegeCode = this.dataset.id;
            if (confirm('Are you sure you want to delete this college?')) {
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = `/deletecollege/${collegeCode}`;
                const hiddenInput = document.createElement('input');
                hiddenInput.type = 'hidden';
                hiddenInput.name = 'csrf_token';
                hiddenInput.value = '{{ csrf_token() }}';
                form.appendChild(hiddenInput);
                document.body.appendChild(form);
                form.submit();
            }
        });
    });
}

// Bind initial table buttons
bindActionButtons();
