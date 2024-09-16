$(document).ready(function() {
   
    $('#addModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); 
        var actionType = button.text().trim();  
        var url = (actionType === 'Add Student') ? '/add' : '/update';

        // Load content from the appropriate route
        $('#addModalBody').load(url);
    });
});