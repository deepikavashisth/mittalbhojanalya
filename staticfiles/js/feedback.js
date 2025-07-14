function getCSRFToken() {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, 10) === ('csrftoken=')) {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
function openFeedback() {
    document.getElementById("feedbackForm").style.display = "block";
}

function closeFeedback() {
    document.getElementById("feedbackForm").style.display = "none";
}

function submitFeedback() {
    var name = document.getElementById("feedbackName").value;
    var message = document.getElementById("feedbackMessage").value;
    alert("Thank you " + name + " for your feedback!");
    closeFeedback();
}

function closeDiscount() {
    document.getElementById("discountPopup").style.display = "none";
}

window.onload = function() {
  let slideIndex = 0;
  const slides = document.querySelectorAll('.banner-slider img');
  const dots = document.querySelectorAll('.dot');
  const slider = document.querySelector('.banner-slider');

  function moveSlide() {
    slider.style.transform = `translateX(-${slideIndex * 100}%)`;
    dots.forEach(dot => dot.classList.remove('active'));
    dots[slideIndex].classList.add('active');
    slideIndex = (slideIndex + 1) % slides.length;
  }

  setInterval(moveSlide, 4000);
};
document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("subscribeModal");
const subscribeBtn = document.getElementById("subscribeBtn");
const closeBtn = document.querySelector("#subscribeModal .close");

  const subscribeForm = document.getElementById("subscribeForm");

if (subscribeBtn) {
  subscribeBtn.onclick = function () {
    modal.style.display = "block";
  }
}

if (closeBtn) {
  closeBtn.onclick = function () {
    modal.style.display = "none";
  }
}

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
  if (subscribeForm) {
    subscribeForm.addEventListener("submit", function (e) {
      e.preventDefault();

      const formData = new FormData(subscribeForm);

      fetch("/ajax/subscribe/", {
        method: "POST",
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': getCSRFToken()

        },
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        const messageDiv = document.getElementById("subscribe-message");
        if (data.status === "success") {
          messageDiv.innerHTML = "<span style='color:green;'>Thank you for subscribing!</span>";
          setTimeout(() => {
            document.getElementById("subscribeModal").style.display = "none";
            subscribeForm.reset();
            messageDiv.innerHTML = "";
          }, 2000);
        } else {
          messageDiv.innerHTML = "<span style='color:red;'>Please check your details.</span>";
        }
      })
      .catch(error => {
        console.error("Error:", error);
      });
    });
  }
});





