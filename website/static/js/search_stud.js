document.getElementById('ShowDetails').addEventListener('click', function() {

                document.getElementById('firstName').readOnly = true;
                document.getElementById('lastName').readOnly = true;
                document.getElementById('program').disabled = true;
                document.getElementById('gender').disabled = true;
                document.getElementById('year').readOnly = true;
            
                document.getElementById('doneButton').style.display = 'none';
                document.getElementById('deletestud').style.display = 'none';
                document.getElementById('cancelstud').style.display = 'none';
                document.getElementById('updateimage').style.display = 'none';
                 document.getElementById('updateimage').style.display = 'none';
            
                document.getElementById('editButton').style.display = 'block';
                document.getElementById('searchStudentModalLabel').textContent = 'Student Information';

                 $('#searchStudentModal').modal('show');
});


document.getElementById('editButton').addEventListener('click', function() {
   
     document.getElementById('firstName').readOnly = false;
        document.getElementById('lastName').readOnly = false;
        document.getElementById('program').disabled = false;
        document.getElementById('gender').disabled = false;
        document.getElementById('year').readOnly = false;

        document.getElementById('doneButton').style.display = 'block';
        document.getElementById('deletestud').style.display = 'block';
        document.getElementById('cancelstud').style.display = 'block';
        document.getElementById('updateimage').style.display = 'block';

   
    document.getElementById('editButton').style.display = 'none';
    document.getElementById('searchStudentModalLabel').textContent = 'Edit Student Information';
    document.getElementById('addStudentForm').action = '/edit/' + document.getElementById('studentID').value;

    document.getElementById('doneButton').textContent = 'SAVE';

});

document.getElementById('cancelstud').addEventListener('click', function() {

    document.getElementById('firstName').readOnly = true;
    document.getElementById('lastName').readOnly = true;
    document.getElementById('program').disabled = true;
    document.getElementById('gender').disabled = true;
    document.getElementById('year').readOnly = true;

    document.getElementById('doneButton').style.display = 'none';
    document.getElementById('deletestud').style.display = 'none';
    document.getElementById('cancelstud').style.display = 'none';
    document.getElementById('updateimage').style.display = 'none';

    document.getElementById('editButton').style.display = 'block';
    document.getElementById('searchStudentModalLabel').textContent = 'Student Information';


});

document.getElementById('closebutton').addEventListener('click', function() {

    document.getElementById('firstName').readOnly = true;
    document.getElementById('lastName').readOnly = true;
    document.getElementById('program').disabled = true;
    document.getElementById('gender').disabled = true;
    document.getElementById('year').readOnly = true;

    document.getElementById('doneButton').style.display = 'none';
    document.getElementById('deletestud').style.display = 'none';
    document.getElementById('cancelstud').style.display = 'none';
    document.getElementById('updateimage').style.display = 'none';

    document.getElementById('editButton').style.display = 'block';
    document.getElementById('searchStudentModalLabel').textContent = 'Student Information';


});

document.getElementById('deletestud').addEventListener('click', function() {
    const studentID = document.getElementById('studentID').value;

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
});

