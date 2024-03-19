import React from "react";
import "./Recipe.css";

const Recipe = ({ data: { name, steps, ingredients, preparationTime, cookingTime, calories } }) =>
    <div className="recipe-card">
        <div className="recipe-stats">
            <span title="Cooking Time">&#129379; {preparationTime}</span>
            <span title="Preparation Time">&#127859; {cookingTime}</span>
            <span title="Calories">&#127869; {calories}</span>
        </div>
        <div className="recipe-content">
            <h1>{name}</h1>
            <div className="ingredients">
                <h2>Ingredients</h2>
                <ul>
                    {ingredients?.map((step, i) => <li key={`ingredient-${i}`}>{step}</li>)}
                </ul>
            </div>

            <div className="steps">
                <h2>Steps</h2>
                <ol>
                    {steps?.map((step, i) => <li key={`step-${i}`}>{step}</li>)}
                </ol>
            </div>
        </div>
    </div>;

export default Recipe;
