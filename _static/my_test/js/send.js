console.log(1);

let inputbox = document.getElementById('id_subtraction_answer');
console.log(inputbox);

function liveRecv(data) {
  history.innerHTML += data.id_in_group + ":" + data.subtraction_answer;
}

function sendValue() {
  liveSend(parseInt(inputbox.value));
}
