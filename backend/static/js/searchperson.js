var cat;

  document.getElementById("name").addEventListener("click", function() {
    cat = "name";
    document.getElementById("cat-input").value = cat;  // Assign the value to the hidden input field
    console.log(cat);
  });

  document.getElementById("occupation").addEventListener("click", function() {
    cat = "occupation";
    document.getElementById("cat-input").value = cat;  // Assign the value to the hidden input field
    console.log(cat);
  });

  document.getElementById("age_less_than").addEventListener("click", function() {
    cat = "age_less_than";
    document.getElementById("cat-input").value = cat;  // Assign the value to the hidden input field
    console.log(cat);
  });

  document.getElementById("age_greater_than").addEventListener("click", function() {
    cat = "age_greater_than";
    document.getElementById("cat-input").value = cat;  // Assign the value to the hidden input field
    console.log(cat);
  });

  document.getElementById("familynumber").addEventListener("click", function() {
    cat = "familynumber";
    document.getElementById("cat-input").value = cat;  // Assign the value to the hidden input field
    console.log(cat);
  });

const buttons = document.getElementsByClassName('filterbutton');

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    buttons[i].classList.add('clicked'); // Add the 'clicked' class to the clicked button
  });
}