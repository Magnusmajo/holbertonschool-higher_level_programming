document.addEventListener('DOMContentLoaded', async function () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    const data = await response.json();
    const characterName = data.name;

    const characterElement = document.getElementById('character');
    characterElement.textContent = characterName;
  } catch (error) {
    console.error('Error fetching character data:', error);
  }
});
