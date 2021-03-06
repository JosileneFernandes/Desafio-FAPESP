const express = require('express')
const routes = express.Router()

// let login =[
//    { Usuario:'tech', Senha:'123'}

// ]
// let token =[
//     {token:'token_de_acesso'}
// ]

// Pegar informação através de get passando um token auth e apresentar como lista
routes.get('/pesos', (req,res)=>{

    const headers = req.headers
    const fs = require("fs")    
      
    const jsonData = JSON.parse(fs.readFileSync("./pesos.json" , "utf8")) 
    if(headers.token === 'token_de_acesso'){
        return res.json(jsonData)    
    }

    else{
        return res.status(400).end()
    }
    
})
// filtrar por lote
routes.get('/pesos/:lote', (req,res)=>{

    const headers = req.headers
    const id_lote = parseInt(req.params.lote)
    const fs = require("fs")    
    
    function buscarLote(value) {        
        return value.idlote === id_lote;        
    }
      
    const jsonData = JSON.parse(fs.readFileSync("./pesos.json" , "utf8")) 
    if(headers.token === 'token_de_acesso'){

        const lote = jsonData.filter(buscarLote)   
        return res.json(lote)
    }
    else{
        return res.status(400).end()
    }    
})


//autenticação login
routes.post('/login', (req,res,next) =>{
    const body = req.body
    
    if(body.user === 'tech' && body.pwd === '123'){
        
        return res.json(token)
    
    }
    else{
        return res.status(400).end()
    }
    
})

module.exports = routes