
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



///////////////////////////////////////////////////////////////////////////////////////////////////


function getMilk(bottles) {   
    console.log("leaveHouse");
    console.log("moveRight");
    console.log("moveRight");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveUp");
    console.log("moveRight");
    console.log("moveRight");
    console.log("buy" + bottles + "bottles of Milk");
    console.log("moveLeft");
    console.log("moveLeft");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveDown");
    console.log("moveLeft");
    console.log("moveLeft");
    console.log("enterHouse");
  }

  getMilk(12);




  ///////////////////////////////////////////////////////////////////////////////

///////////////  Life in Weeks Coding Exercise////////////////////


  function lifeInWeeks(age) {
    // Calculate the number of days, weeks, and months left until 90 years old
    const daysLeft = (90 - age) * 365;
    const weeksLeft = (90 - age) * 52;
    const monthsLeft = (90 - age) * 12;
  
    // Print the message
    console.log(`You have ${daysLeft} days, ${weeksLeft} weeks, and ${monthsLeft} months left.`);
  }
  


  //////////////////////////////////////////////////////////////////////
  ///////////////////BMI Calculator////////////////////////////////////


  function classifyBMI(height, weight) {
    const bmi = weight / (height * height);
  
    if (bmi < 18.5) {
      return "Underweight";
    } else if (bmi < 25) {
      return "Normal";
    } else if (bmi < 30) {
      return "Overweight";
    } else {
      return "Obese";
    }
  }
  
  console.log(classifyBMI(1.75, 75)); // Output: Normal
  




  ///////////////////////////////////////////////////////////////////////
  ////////////////// While Statement - 99 Bottles Problem ////////////////////////////////////
  var numberOfBottles = 99
while (numberOfBottles >= 0) {
    var bottleWord = "bottle";
    if (numberOfBottles === 1) {
        bottleWord = "bottles";
    } 
    console.log(numberOfBottles + " " + bottleWord + " of beer on the wall");
    console.log(numberOfBottles + " " + bottleWord + " of beer,");
    console.log("Take one down, pass it around,");
	numberOfBottles--;
    console.log(numberOfBottles + " " + bottleWord + " of beer on the wall.");