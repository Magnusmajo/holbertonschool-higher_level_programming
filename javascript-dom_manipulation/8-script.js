document.addEventListener('DOMContentLoaded', async function () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    const translatedHello = data.hello;

    const helloElement = document.getElementById('hello');

    helloElement.textContent = translatedHello;
  } catch (error) {
    console.error('Error fetching translation:', error);
  }
});
