document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Get form values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // For demo purposes, just log the data
    console.log(`Username: ${username}`);
    console.log(`Password: ${password}`);
    console.log(`Role: ${role}`);

    // Normally, you would send this data to a server using an AJAX request
    alert(`Logged in as ${role}`);
});
