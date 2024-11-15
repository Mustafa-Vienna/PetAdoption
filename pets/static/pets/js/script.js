const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);


$(document).ready(() => {
  setTimeout(() => {
    $("#successMsg").fadeOut().empty();
  }, 3000);
  $(".comment-form")[0]?.reset();
});