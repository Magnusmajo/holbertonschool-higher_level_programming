document.addEventListener('DOMContentLoaded', async function () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const data = await response.json();
    const movieList = document.getElementById('list_movies');

    data.results.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  } catch (error) {
    console.error('Error fetching movie data:', error);
  }
});
