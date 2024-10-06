document.getElementById('searchCollegeBtn').addEventListener('click', function() {
    const query = document.getElementById('collegeinput').value;

    // Make a GET request to the search route with the query (either code or name)
    fetch(`/search_college?query=${query}`)
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data:', data);

            if (data) {
                // If the college is found, populate the fields
                document.getElementById('collegeCode').value = data.code;
                document.getElementById('collegeName').value = data.name;

                // Show the modal with college info
                $('#searchcollege').modal('show');

                // Make fields read-only and hide action buttons (edit mode)
                document.getElementById('collegeCode').readOnly = true;
                document.getElementById('collegeName').readOnly = true;

                document.getElementById('donecollege').style.display = 'none';
                document.getElementById('deletecollege').style.display = 'none';
                document.getElementById('cancelcollege').style.display = 'none';

                document.getElementById('editcollege').style.display = 'block';
                document.getElementById('searchcollegelabel').textContent = 'College Information';
            } else {
                alert('College not found');
            }
        })
        .catch(error => console.error('Error fetching college data:', error));
});


document.getElementById('editcollege').addEventListener('click', function() {
    document.getElementById('collegeCode').readOnly = false;  // Allow editing code now
    document.getElementById('collegeName').readOnly = false;

    document.getElementById('donecollege').style.display = 'block';
    document.getElementById('deletecollege').style.display = 'block';
    document.getElementById('cancelcollege').style.display = 'block';

    document.getElementById('editcollege').style.display = 'none';
    document.getElementById('searchcollegelabel').textContent = 'Edit College Information';
  
    document.getElementById('addcollegeForm').action = '/updatecollege/' + document.getElementById('collegeCode').value;
    document.getElementById('donecollege').textContent = 'SAVE';
});

document.getElementById('cancelcollege').addEventListener('click', function() {
    document.getElementById('collegeCode').readOnly = true;
    document.getElementById('collegeName').readOnly = true;

    document.getElementById('donecollege').style.display = 'none';
    document.getElementById('deletecollege').style.display = 'none';
    document.getElementById('cancelcollege').style.display = 'none';
 
    document.getElementById('editcollege').style.display = 'block';
    document.getElementById('searchcollegelabel').textContent = 'College Information';
});

document.getElementById('deletecollege').addEventListener('click', function() {
    const collegeCode = document.getElementById('collegeCode').value;

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


