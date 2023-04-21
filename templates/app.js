const recordButton = document.getElementById("recordButton");
const stopButton = document.getElementById("stopButton");
const sendButton = document.getElementById("sendButton");

let mediaRecorder;
let recordedAudio;

recordButton.addEventListener("click", async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.start();
    recordButton.disabled = true;
    stopButton.disabled = false;
    sendButton.disabled = true;

    mediaRecorder.addEventListener("dataavailable", (event) => {
        if (event.data.size > 0) {
            recordedAudio = event.data;
        }
    });
});

stopButton.addEventListener("click", () => {
    mediaRecorder.stop();
    recordButton.disabled = false;
    stopButton.disabled = true;
    sendButton.disabled = false;
});

sendButton.addEventListener("click", async () => {
    if (!recordedAudio) {
        alert("Please record audio first");
        return;
    }

    const formData = new FormData();
    formData.append("audio", recordedAudio, "my-recording.webm");

    try {
        const response = await fetch("https://your-webserver-url.com/upload", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            alert("Audio sent successfully");
            sendButton.disabled = true;
        } else {
            alert("Error sending audio");
        }
    } catch (error) {
        console.error(error);
        alert("Error sending audio");
    }
});