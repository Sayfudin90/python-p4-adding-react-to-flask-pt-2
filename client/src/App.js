import { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);
  
  useEffect(() => {
    fetch("/movies")
      .then((r) => r.json())
      .then((movieData) => {
        console.log(movieData);
        setMovies(movieData);
      });
  }, []);

  return (
    <div className="App">
      <h1>Movies from Flask API</h1>
      <h2>Check the console for a list of movies!</h2>
      
      {movies.length > 0 && (
        <div>
          <h3>Movies:</h3>
          <ul>
            {movies.map(movie => (
              <li key={movie.id}>
                {movie.title} ({movie.year}) - {movie.genre}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;