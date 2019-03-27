// box asking for the users name //
function visitorName() {
  var txt;
  var person = prompt("Please enter your name:", "e.g Harry Potter");
  localStorage.setItem(person)
  if (person == null || person == "") {
    txt = "User cancelled the prompt.";
  }
  else {
    localStorage.setItem(person);
    return person
  }
}
