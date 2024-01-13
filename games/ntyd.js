const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');
const startButton = document.getElementById('start-button');

let gameStarted = false;
let gameOver = false;
let timeLeft = 5;

canvas.width = 800;
canvas.height = 600;

const player = {
    x: canvas.width / 2,
    y: canvas.height - 100,
    size: 50,
};

const savedMan = {
    x: canvas.width / 2,
    y: canvas.height - 200,
    size: 50,
};

const car = {
    x: canvas.width / 2,
    y: canvas.height - 150,
    size: 50,
    speed: 2,
};

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (!gameOver) {
        ctx.fillStyle = '#333';
        ctx.fillRect(player.x, player.y, player.size, player.size);

        ctx.fillStyle = '#00f';
        ctx.fillRect(savedMan.x, savedMan.y, savedMan.size, savedMan.size);

        ctx.fillStyle = '#f00';
        ctx.fillRect(car.x, car.y, car.size, car.size);

        if (gameStarted) {
            timeLeft--;
            if (timeLeft <= 0) {
                gameOver = true;
                ctx.fillStyle = '#f00';
                ctx.font = 'bold 32px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('Game Over', canvas.width / 2, canvas.height / 2);
            } else {
                ctx.fillStyle = '#000';
                ctx.font = 'bold 24px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(`Time Left: ${timeLeft}`, canvas.width / 2, 50);
            }

            car.x -= car.speed;
            if (car.x + car.size < 0) {
                car.x = canvas.width;
            }

            if (
                player.x + player.size > savedMan.x &&
                player.x < savedMan.x + savedMan.size &&
                player.y + player.size > savedMan.y &&
                player.y < savedMan.y + savedMan.size
            ) {
                gameOver = true;
                ctx.fillStyle = '#0f0';
                ctx.font = 'bold 32px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('You Saved Him!', canvas.width / 2, canvas.height / 2);
            }
        }
    } else {
        ctx.fillStyle = '#000';
        ctx.font = 'bold 32px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('Game Over', canvas.width / 2, canvas.height / 2);
    }
}

startButton.addEventListener('click', () => {
    gameStarted = true;
    timeLeft = 5;
});

setInterval(draw, 1000 / 60);
