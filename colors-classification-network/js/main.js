document.addEventListener('DOMContentLoaded', function () {
    
    // Get input color
    let colorInput = document.getElementById('color-input');
    let subtitleElement = document.getElementById('subtitle');

    // Change color event updating and calling jscolor
    colorInput.addEventListener('input', function () {
        update(this.jscolor);
        classifyColor(this.jscolor);
    });

    // Starting network
    let network = new brain.NeuralNetwork();

    //Classifing network
    let classificatorNetwork = new brain.NeuralNetwork();
    
    //Training network
    network.train([
        // Black background (input all 0s) = white text (output=1)
        { input: { red: 0, green: 0, blue: 0 }, output: { color: 1 } },
        // White background (input all 1s) = black text (output=0)
        { input: { red: 1, green: 1, blue: 1 }, output: { color: 0 } },
        // Green background (input green=1) = white text (output=0)
        { input: { red: 0, green: 1, blue: 0 }, output: { color: 0 } },
        // Blue background (input blue=1) = white text (output=1)
        { input: { red: 0, green: 0, blue: 1 }, output: { color: 1 } },
        // Red background (input red=1) = white text (output=1)
        { input: { red: 1, green: 0, blue: 0 }, output: { color: 1 } }
    ])

    // Traning network with colors names
    classificatorNetwork.train([
        { input: { red: 0, green: 1, blue: 0 }, output: { 'verde': 1, 'azul': 0, 'rojo': 0 } },
        { input: { red: 0, green: 0, blue: 1 }, output: { 'verde': 0, 'azul': 1, 'rojo': 0 } },
        { input: { red: 1, green: 0, blue: 0 }, output: { 'verde': 0, 'azul': 0, 'rojo': 1 } },
        { input: { red: 1, green: 1, blue: 0 }, output: { 'amarillo': 1, 'verde': 0, 'azul': 0, 'rojo': 0 } },
        { input: { red: 1, green: 0.5, blue: 0 }, output: { 'naranja': 1, 'verde': 0, 'azul': 0, 'rojo': 0 } },
        { input: { red: 0.5, green: 0.5, blue: 1 }, output: { 'morado': 1, 'verde': 0, 'azul': 0, 'rojo': 0 } },
    ]);
    

    function classifyColor(color) {
        
        // Get RGB values
        let rgb = [color.channels.r, color.channels.g, color.channels.b];

        // Get element
        let classificator = document.getElementById("classificator");
    
        // Normalize RGB values on range [0, 1]
        let colorInput = {
            red: rgb[0] / 255,
            green: rgb[1] / 255,
            blue: rgb[2] / 255
        }

        // Network gets color selected
        let colorOutput = classificatorNetwork.run(colorInput);
        console.log(JSON.stringify(colorOutput, null, 2));

        // Get color name with most probability
        let colorName = Object.keys(colorOutput).reduce((a, b) => colorOutput[a] > colorOutput[b] ? a : b);
        
        // Get color value
        let colorProbability  = colorOutput[colorName].toFixed(3); // Rounded 3 decimals
        console.log('colorvalue - ' + colorProbability )

        
        // Set text color to match the background color
        subtitleElement.style.color = color.toHEXString();
        
        //Add text with color value and name
        classificator.textContent = 'Color de fondo: ' + colorName + ' - Probabilidad: ' + (colorProbability * 100).toFixed(2) + '%';
    }
    
    function update(color) {

        let rgb = [color.channels.r, color.channels.g, color.channels.b];
        let title = document.getElementById("title");
        
        title.style.backgroundColor = color.toHEXString();

        let colorInput = {
            red: rgb[0] / 255,
            green: rgb[1] / 255,
            blue: rgb[2] / 255
        }

        let colorOutput = network.run(colorInput);

        if (colorOutput.color > 0.5) {
            title.style.color = "white";
        } else {
            title.style.color = "black";
        }
    }
});
