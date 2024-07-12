function updateDate() {
    const dateElement = document.querySelector('.nav-date');
    const now = new Date();
    const days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'];
    const months = [
        'Jan', 'Feb', 'Mar', 'April', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ];
    const day = days[now.getDay()];
    const date = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();

    dateElement.textContent = `${day}, ${date} ${month}, ${year}`;
}

async function fetchTemperature() {
    const apiKey = '99ca9aef568f48fda9e90259240607';
    const city = 'New Delhi';
    const url = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const temperature = data.current.temp_c;

        document.querySelector('.nav-weather').textContent = `New Delhi ${temperature}°C`;
    } catch (error) {
        document.querySelector('.nav-weather').textContent = 'Error fetching temperature';
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Call the function to update the date when the page loads
updateDate();

// Call the function to fetch the temperature when the page loads
fetchTemperature();