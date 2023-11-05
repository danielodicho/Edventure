// Replace the placeholder functions and variables with actual implementations

// Placeholder function to start the camera
// function startCamera() {
//     const video = document.getElementById('cameraPreview');
//     if (navigator.mediaDevices.getUserMedia) {
//         navigator.mediaDevices.getUserMedia({ video: true })
//             .then(function(stream) {
//                 video.srcObject = stream;
//             })
//             .catch(function(error) {
//                 console.log("Something went wrong!");
//             });
//     }
// }


function startCamera() {
    const video = document.getElementById('cameraPreview');
    const constraints = {
        video: { facingMode: { exact: "environment" } } // This will attempt to use the back camera
    };

    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia(constraints)
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function(error) {
                console.log("Something went wrong!", error);
            });
    }
}

// Placeholder function to capture an image
function captureImage() {
    const canvas = document.createElement('canvas');
    const video = document.getElementById('cameraPreview');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    
    // Convert the canvas image to a data URL and send it
    const dataUrl = canvas.toDataURL('image/png');
    sendImage(dataUrl);
}
function sendImage(dataUrl) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/save-image', true); // Assume '/save-image' is the endpoint
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ image: dataUrl }));

    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log('Image saved successfully');
        } else {
            console.log('Error saving image');
        }
    };
}

function showScreen(screenId) {
    console.log("showScreen called with:", screenId);
    // Hide all screens
    document.querySelectorAll('.screen').forEach(screen => {
        screen.style.display = 'none';
    });
    // Show the requested screen
    const screenToShow = document.getElementById(screenId);
    if (screenToShow) {
        screenToShow.style.display = 'block';
    } else {
        console.error('No screen found with ID:', screenId); // Error if no screen is found
    }

}

// function initAutocomplete() {
//     const input = document.getElementById('destinationInput');
//     const autocomplete = new google.maps.places.Autocomplete(input);
//
//     autocomplete.addListener('place_changed', function () {
//         const place = autocomplete.getPlace();
//         console.log('Place selected: ', place.formatted_address);
//         // Handle the selected place information
//     });
// }
document.addEventListener('DOMContentLoaded', function() {
    // Set the user's name if necessary
    //document.getElementById('userName').textContent = 'Yejun'; // Replace 'Your Name' as needed
    //initAutocomplete();
    // Handle the "Start Trip" button click
    document.getElementById('startTripBtn').addEventListener('click', function() {
        console.log("'Start Trip' button clicked");
        showScreen('cameraScreen');
        startCamera();
    });

    document.getElementById('destinationInput').addEventListener('change', function() {
        console.log("typing destination");
        showScreen('cameraScreen');
        //document.getElementById('destinationInput').trigger("geocode");
    });


    document.getElementById('loginBtn').addEventListener('click', function() {
        console.log("'Login' button clicked");
        showScreen('welcomeScreen');
        startCamera();
    });
    //
    // // Handle the "Select Destination" button click
    // document.getElementById('selectDestinationBtn').addEventListener('click', function() {
    //     // Implement destination selection using Google Places API
    //     // ...
    //     // showScreen('travelModesScreen');
    // });
    //
    // // Handle travel mode selection
    // document.querySelectorAll('#travelModesScreen button').forEach(button => {
    //     button.addEventListener('click', function() {
    //         // Save the selected travel mode if needed
    //         // ...
    //         //showScreen('cameraScreen');
    //         // startCamera();
    //     });
    // });

    // Handle the capture button click
    document.getElementById('captureBtn').addEventListener('click', function() {
        // captureImage();
        showScreen('welcomeScreen');
    });

    document.querySelectorAll('.travel-mode-item').forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all items
            document.querySelectorAll('.travel-mode-item').forEach(i => {
                i.classList.remove('active');
            });
            // Add active class to the clicked item
            item.classList.add('active');
            // Handle the travel mode selection here...
            console.log('Selected travel mode:', item.dataset.mode);
        });
    });


    // Handle all "Go Back" button clicks
    document.querySelectorAll('.goBackBtn').forEach(button => {
        button.addEventListener('click', function(event) {
            const currentScreen = event.target.closest('.screen');
            // Determine which screen to go back to
            if (currentScreen.id === 'cameraScreen') {
                showScreen('welcomeScreen');
            } else if (currentScreen.id === 'welcomeScreen') {
                showScreen('loginScreen');
            }
            // } else if (currentScreen.id === 'cameraScreen') {
            //     showScreen('travelModesScreen');
            // }
        });
    });


});




