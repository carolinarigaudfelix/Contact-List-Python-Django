function confirmDelete(event) {
    event.preventDefault(); 
    if (confirm("Are you sure you would like to delete this contact?")) 
        {document.getElementById("delete-form").submit() ;}
        alert("Contact deleted successfully!");
}    

