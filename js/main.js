// UI variables
const navToggler = document.querySelector(".nav-toggler");
const navMenu = document.querySelector(".site-navbar ul");
const navLinks = document.querySelectorAll(".site-navbar a");
const getStartedBtnDesktop = document.getElementById("getStartedBtnDesktop");
const getStartedBtnMobile = document.getElementById("getStartedBtnMobile");
const popupForm = document.getElementById("popupForm");
const closePopup = document.getElementById("closePopup");
const cancelBtn = document.getElementById("cancelBtn");
const popupFormContent = document.getElementById("popupFormContent");

// Event listeners
allEventListeners();

function allEventListeners() {
  navToggler.addEventListener("click", togglerClick); // Toggler icon click event
  navLinks.forEach((elem) => elem.addEventListener("click", navLinkClick)); // Nav links click event
  if (getStartedBtnDesktop) {
    getStartedBtnDesktop.addEventListener("click", showPopup); // Get Started button click event (Desktop)
  }
  if (getStartedBtnMobile) {
    getStartedBtnMobile.addEventListener("click", showPopup); // Get Started button click event (Mobile)
  }
  if (closePopup) {
    closePopup.addEventListener("click", closePopupForm); // Close popup events
  }
  if (cancelBtn) {
    cancelBtn.addEventListener("click", closePopupForm); // Cancel button click event
  }
  if (popupFormContent) {
    popupFormContent.addEventListener("submit", handleFormSubmit); // Popup form submission event
  }
  window.addEventListener("scroll", highlightNavLink); // Nav link highlighting on scroll
  highlightNavLink(); // Initial highlighting
}

// Toggler click function
function togglerClick() {
  navToggler.classList.toggle("toggler-open");
  navMenu.classList.toggle("open");
}

// Nav link click function
function navLinkClick() {
  if (navMenu.classList.contains("open")) {
    navToggler.click();
  }
}

// Show popup function with animation
function showPopup() {
  popupForm.classList.add("open");
}

// Close popup function with animation
function closePopupForm() {
  popupForm.classList.remove("open");
}

// Handle form submit function
function handleFormSubmit(event) {
  event.preventDefault();

  // Get form data
  const form = document.getElementById("popupFormContent");
  const formData = new FormData(form);
  const enteredName = formData.get("name"); // Retrieve entered name

  // Show loading message with personalized greeting
  showLoadingMessage(enteredName);

  // Redirect to selected city page after delay
  setTimeout(() => {
    const selectedCity = formData.get("city");
    switch (selectedCity) {
      case "bangalore":
        window.location.href = "/pages/City/bangalore.html";
        break;
      case "hyderabad":
        window.location.href = "/pages/City/hyderabad.html";
        break;
      case "mumbai":
        window.location.href = "/pages/City/mumbai.html";
        break;
      case "delhi":
        window.location.href = "/pages/City/delhi.html";
        break;
      default:
        console.error("Invalid city selection.");
        break;
    }
  }, 4000); // 4 seconds delay
}

// Function to show loading message with personalized greeting
function showLoadingMessage(name) {
  const loadingMessage = document.createElement("div");
  loadingMessage.innerHTML = `Hello ${name}...<br>Choosing best experience for you`;
  loadingMessage.style.position = "fixed";
  loadingMessage.style.top = "50%";
  loadingMessage.style.left = "50%";
  loadingMessage.style.transform = "translate(-50%, -50%)";
  loadingMessage.style.background = "#ffe37ee3";
  loadingMessage.style.color = "rgb(51, 51, 51)";
  loadingMessage.style.padding = "20px";
  loadingMessage.style.borderRadius = "8px";
  loadingMessage.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.1)";
  loadingMessage.style.zIndex = "1000";
  loadingMessage.style.textAlign = "center";
  loadingMessage.style.fontSize = "18px";
  loadingMessage.style.display = "inline-block";
  loadingMessage.style.whiteSpace = "nowrap"; // Prevent text wrapping

  // Create overlay with blur effect
  const body = document.body;
  const overlay = document.createElement("div");
  overlay.id = "blur-overlay";
  overlay.style.position = "fixed";
  overlay.style.top = "0";
  overlay.style.left = "0";
  overlay.style.width = "100%";
  overlay.style.height = "100%";
  overlay.style.backgroundColor = "rgba(255, 255, 255, 0.5)";
  overlay.style.backdropFilter = "blur(10px)";
  overlay.style.zIndex = "999";
  body.appendChild(overlay);

  // Append loading message to overlay
  overlay.appendChild(loadingMessage);

  // Remove loading message and overlay after delay
  setTimeout(() => {
    overlay.remove();
  }, 4000);
}

// Highlight nav link on scroll
function highlightNavLink() {
  const sections = document.querySelectorAll("section");
  let current = "home"; // Default active section

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (window.scrollY >= sectionTop - sectionHeight / 3) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href") === `#${current}`) {
      link.classList.add("active");
    }
  });
}

// Hero section text animation
const cityNames = ["Bangalore", "Hyderabad", "Mumbai", "Delhi"];
let index = 0;
let isDeleting = false;
let currentText = "";
let typingSpeed = 200; // Typing speed in milliseconds

function typeCityName() {
  const cityNameElement = document.getElementById("city-name");
  const currentCity = cityNames[index];
  if (isDeleting) {
    currentText = currentCity.substring(0, currentText.length - 1);
  } else {
    currentText = currentCity.substring(0, currentText.length + 1);
  }

  cityNameElement.textContent = currentText;

  let typingDelay = typingSpeed;
  if (isDeleting) {
    typingDelay /= 2;
  }

  if (!isDeleting && currentText === currentCity) {
    typingDelay = 1000; // Pause at end of typing
    isDeleting = true;
  } else if (isDeleting && currentText === "") {
    isDeleting = false;
    index = (index + 1) % cityNames.length;
    typingDelay = 500; // Pause before typing next city
  }

  setTimeout(typeCityName, typingDelay);
}

// Start typing animation on page load
window.onload = function () {
  typeCityName();
};

// Feedback form submission handling
document
  .getElementById("feedbackForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    setTimeout(function () {
      document.getElementById("submitMessage").style.display = "block"; // Display submit message
      document.getElementById("feedbackForm").reset(); // Reset form after submission
    }, 1000); // 1 second delay
  });

// faq section code
document.querySelectorAll(".accordion-header").forEach((button) => {
  button.addEventListener("click", () => {
    const accordionContent = button.nextElementSibling;

    button.classList.toggle("active");

    if (button.classList.contains("active")) {
      accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
    } else {
      accordionContent.style.maxHeight = 0;
    }

    // Close other open accordion items
    document.querySelectorAll(".accordion-header").forEach((otherButton) => {
      if (otherButton !== button) {
        otherButton.classList.remove("active");
        otherButton.nextElementSibling.style.maxHeight = 0;
      }
    });
  });
});
