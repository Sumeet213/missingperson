const util = require("util");
const multer = require("multer");
const maxSize = 2 * 1024 * 1024;

let storage = multer.diskStorage({
  destination: (req, file, cb) => {
    let directory = "./resources/static/assets/uploads/"

    
    console.log("hey here",typeof req.body.folder);
    //folder==> 0 missing cases-->known cases   
    //folder==>1 reported cases --> unknown cases
    if (req.body.folder === "1" ) {
      cb(null,  directory+'known');
    } else {
      cb(null,directory+ 'unknown');
    }
    // cb(null, __basedir + "/resources/static/assets/uploads/");
  },
  filename: (req, file, cb) => {
      
    console.log(file.originalname);
    cb(null, file.originalname);
  },
});

let uploadFile = multer({
  storage: storage,
  limits: { fileSize: maxSize },
}).single("file");

let uploadFileMiddleware = util.promisify(uploadFile);
module.exports = uploadFileMiddleware;
