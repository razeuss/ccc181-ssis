document.getElementById('searchButton').addEventListener('click', function() {
    const studentID = document.getElementById('studentSearch').value;

    // Fetch student data from the server
    fetch(`/student/${studentID}`)
        .then(response => response.json())
        .then(data => {
            if (data) {
               
                document.getElementById('firstName').value = data.firstname;
                document.getElementById('lastName').value = data.lastname;
                document.getElementById('studentID').value = data.id;
                document.getElementById('program').value = data.program_code;
                document.getElementById('gender').value = data.gender;
                document.getElementById('year').value = data.year;

                $('#searchStudentModal').modal('show');
            } else {
                alert('Student not found');
            }
        })
        .catch(error => console.error('Error fetching student data:', error));
});


document.getElementById('searchButton').addEventListener('click', function() {

    document.getElementById('firstName').readOnly = true;
    document.getElementById('lastName').readOnly = true;
    document.getElementById('program').readOnly = true;
    document.getElementById('gender').disabled = true;
    document.getElementById('year').readOnly = true;

    document.getElementById('doneButton').style.display = 'none';
    document.getElementById('deleteButton').style.display = 'none';
    document.getElementById('cancelButton').style.display = 'none';

    document.getElementById('editButton').style.display = 'block';
    document.getElementById('searchStudentModalLabel').textContent = 'Student Information';


});

document.getElementById('editButton').addEventListener('click', function() {
   
     document.getElementById('firstName').readOnly = false;
        document.getElementById('lastName').readOnly = false;
        document.getElementById('program').readOnly = false;
        document.getElementById('gender').disabled = false;
        document.getElementById('year').readOnly = false;

        document.getElementById('doneButton').style.display = 'block';
        document.getElementById('deleteButton').style.display = 'block';
        document.getElementById('cancelButton').style.display = 'block';

    document.getElementById('doneButton').style.display = 'block';
    document.getElementById('editButton').style.display = 'none';
    document.getElementById('searchStudentModalLabel').textContent = 'Edit Student Information';
    document.getElementById('addStudentForm').action = '/edit/' + document.getElementById('studentID').value;

    document.getElementById('doneButton').textContent = 'SAVE';

});

document.getElementById('cancelButton').addEventListener('click', function() {

    document.getElementById('firstName').readOnly = true;
    document.getElementById('lastName').readOnly = true;
    document.getElementById('program').readOnly = true;
    document.getElementById('gender').disabled = true;
    document.getElementById('year').readOnly = true;

    document.getElementById('doneButton').style.display = 'none';
    document.getElementById('deleteButton').style.display = 'none';
    document.getElementById('cancelButton').style.display = 'none';

    document.getElementById('editButton').style.display = 'block';
    document.getElementById('searchStudentModalLabel').textContent = 'Student Information';


});