
function getName() {
    var name = prompt("What is your name?").toLowerCase();

    var firstChar = name.slice(0,1);

    var upperCaseFirstChar = firstChar.toUpperCase();

    var restOfName = name.slice(1,name.length);

    var capitalisedName = upperCaseFirstChar + restOfName;

    alert("Hello, " + capitalisedName);
}

// Call the above function
getName();