const openBtns = document.querySelectorAll("[data-open-modal]");

openBtns.forEach((elem) => {
  var id = elem.getAttribute("data-id");
  const modal = document.querySelector(`dialog[data-id="${id}"]`);
  const closeBtn = modal.querySelector('[data-close-modal]');

  elem.addEventListener("click", () => modal.showModal());

  closeBtn.addEventListener("click", () => modal.close());
});
