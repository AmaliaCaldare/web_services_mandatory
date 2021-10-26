const  express = require('express');
const app = express();

const axios = require('axios');

const bodyParser = require('body-parser');
require('body-parser-xml')(bodyParser);
app.use(bodyParser.xml());

const multer = require('multer');
const upload = multer({dest: 'csv/'});

app.post('/send-number', async (req, res) => {
    const number = req.body.data;
    console.log("Received number:", number);
    try {
        console.log("Sending number:", number*2)
        const result = await axios.post('http://127.0.0.1:7777/number', { data: number*2  });
        if(result.status === 200) {
            console.log("Successfully sent number to port 7777");
        }
        res.status(200).send();
    }
    catch(err) {
        throw err;
    }

})

let fileName;
app.post('/new-number', upload.single('file'), async (req, res) => {
    const file = req.file;
    if (!file) {
        res.status(500).send({'error': 'Something went wrong'});
        return;
    }    
    fileName = file.filename;
    res.status(200).send();
});

app.get('/get-new-number', async (req, res) => {
     const options = {
         root: __dirname + '/csv/'
     }
     res.status(200).sendFile(fileName, options)
});

const PORT = 3333;
app.listen(PORT, () => {
    console.log('Listening to port', PORT);
});