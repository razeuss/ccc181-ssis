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

                document.getElementById('programCode').readOnly = true;
                document.getElementById('college_code').disabled = true;
                document.getElementById('programName').readOnly = true;
            
                document.getElementById('doneprog').style.display = 'none';
                document.getElementById('deleteprog').style.display = 'none';
                document.getElementById('cancelprog').style.display = 'none';
            
                document.getElementById('editprog').style.display = 'block';
                document.getElementById('searchProgramModalLabel').textContent = 'Program Information';
            } else {
                alert('Program not found');
            }
        })
        .catch(error => console.error('Error fetching program data:', error));
});


document.getElementById('editprog').addEventListener('click', function() {
    document.getElementById('programCode').readOnly = false;  
    document.getElementById('college_code').disabled = false;
    document.getElementById('programName').readOnly = false;

    document.getElementById('doneprog').style.display = 'block';
    document.getElementById('deleteprog').style.display = 'block';
    document.getElementById('cancelprog').style.display = 'block';

    document.getElementById('editprog').style.display = 'none';
    document.getElementById('searchProgramModalLabel').textContent = 'Edit Program Information';
  
    document.getElementById('addProgramForm').action = '/update/' + document.getElementById('programCode').value;
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

document.getElementById('deleteprog').addEventListener('click', function() {
    const programCode = document.getElementById('programCode').value;

    if (confirm('Are you sure you want to delete this program?')) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/deleteprog/${programCode}`;

        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'csrf_token';
        hiddenInput.value = '{{ csrf_token() }}'; 

        form.appendChild(hiddenInput);
        document.body.appendChild(form);
        form.submit();
    }
});


document.getElementById('collegeCode').addEventListener('change', function() {
    const selectedCollegeCode = document.getElementById('collegeCode').value;
    window.location.href = `/filter?college_code=${selectedCollegeCode}`;
});

