document.getElementById('searchprog').addEventListener('click', function() {
    const program_code = document.getElementById('programinput').value;

    fetch(`/program/${program_code}`)
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data:', data); 

            if (data) {
                document.getElementById('programCode').value = data.code;
                document.getElementById('college_code').value = data.college_code;
                document.getElementById('programName').value = data.name;

                $('#searchProgramModal').modal('show');
            } else {
                alert('Program not found');
            }
        })
        .catch(error => console.error('Error fetching program data:', error));
});

document.getElementById('searchprog').addEventListener('click', function() {

    document.getElementById('programCode').readOnly = true;
    document.getElementById('college_code').disabled = true;
    document.getElementById('programName').readOnly = true;

    document.getElementById('doneprog').style.display = 'none';
    document.getElementById('deleteprog').style.display = 'none';
    document.getElementById('cancelprog').style.display = 'none';

    document.getElementById('editButton').style.display = 'block';
    document.getElementById('searchStudentModalLabel').textContent = 'Student Information';


});

document.getElementById('editprog').addEventListener('click', function() {
   
  
       document.getElementById('programCode').readOnly = false;
       document.getElementById('college_code').disabled = false;
       document.getElementById('programName').readOnly = false;

       document.getElementById('doneprog').style.display = 'block';
       document.getElementById('deleteprog').style.display = 'block';
       document.getElementById('cancelprog').style.display = 'block';

   document.getElementById('doneprog').style.display = 'block';
   document.getElementById('editprog').style.display = 'none';
   document.getElementById('searchProgramModalLabel').textContent = 'Edit Program Information';
   document.getElementById('addProgramForm').action = '/editprog/' + document.getElementById('college_code').value;

   document.getElementById('doneprog').textContent = 'SAVE';

});

document.getElementById('cancelprog').addEventListener('click', function() {

   document.getElementById('programCode').readOnly = true;
   document.getElementById('college_code').disabled = true;
   document.getElementById('programName').readOnly = true;

   document.getElementById('doneprog').style.display = 'none';
   document.getElementById('deleteprog').style.display = 'none';
   document.getElementById('cancelprog').style.display = 'none';

   document.getElementById('editprog').style.display = 'block';
   document.getElementById('searchProgramModalLabel').textContent = 'Program Information';


});