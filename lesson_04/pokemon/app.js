document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    let data = await fetch(url)
    let pokemonInfo = await data.json()

    console.log(pokemonInfo)
}