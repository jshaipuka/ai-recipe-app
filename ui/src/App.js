import "./App.css";
import React, { useState, useEffect } from "react";
import Recipe from "./Components/Recipe";

const baseApi = process.env.REACT_APP_API_URL ?? 'http://localhost:5000'

function App() {
  const [recipe, setRecipe] = useState({})
  const [search, setSearch] = useState("")
  const [query, setQuery] = useState("")

  useEffect(() => {
    fetchRecipe()
  }, [query])

  const fetchRecipe = async () => {
    console.log(`Query for '${query}'`)

    if (query.trim().length === 0) return

    const response = await fetch(
      `${baseApi}/recipe`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
      })

    const data = await response.json()
    setRecipe(data.recipe)
  }

  const updateSearch = e => setSearch(e.target.value)

  const onSubmit = (e) => {
    e.preventDefault()
    setQuery(search)
  };

  return (
      <div className="App">
        <h1>SEARCH FOR A RECIPE OF YOUR CHOICE</h1>

        <form onSubmit={onSubmit} className="search-form">
          <input
              className="search-bar"
              type="text"
              value={search}
              onChange={updateSearch}
          />
          <button className="search-button" type="submit">
            Search
          </button>
        </form>
        <div className="recipes">
          <Recipe data = {recipe} />
        </div>
      </div>
  )
}

export default App
