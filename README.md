<p align="center">
<img src="images/api.png" width="128" height="128"/>
<br/>
<h3 align="center">Password Generator Rest Api</h3>
<p align="center">Source code for Password-Generator-Rest-API.</p>
<h2></h2>
</p>
<br />

<p align="center">
<a href="../../issues"><img src="https://img.shields.io/github/issues/aminbeigi/Password-Generator-Rest-API.svg?style=flat-square" /></a>
<a href="../../pulls"><img src="https://img.shields.io/github/issues-pr/aminbeigi/Password-Generator-Rest-API.svg?style=flat-square" /></a>
<img src="https://img.shields.io/github/license/aminbeigi/Password-Generator-Rest-API?style=flat-square">
</p>

## Description
Password-Generator-Rest-API takes words as input or randomly generates them from a wordlist and then finds related/similar words. Then the related words are concatenated and made to be more cryptic looking. All this data is put inside a dict and is given to get requests as a response.

## Example
Randomly picking 2 words to generate 2 passwords.  
`.../api/password/random?limit=2`
```json
[
    {
        "words": [
            "bear",
            "control"
        ],
        "related words": [
            "locality",
            "systems"
        ],
        "password": "l.CALItY$YsTEMS"
    },
    {
        "words": [
            "mix",
            "station"
        ],
        "related words": [
            "stereo",
            "subway"
        ],
        "password": "$tereoSubw@y"
    }
]
```
Three user inputted words 'cat', 'computer' and 'apple' to generate 2 passwords.  
`.../api/password?words=cat&words=computer&words=apple&limit=2`
```json
[
    {
        "words": [
            "cat",
            "computer",
            "apple"
        ],
        "related words": [
            "kitten",
            "programmer",
            "ipod"
        ],
        "password": "k!TtENpR.Gr@MMer|PoD"
    },
    {
        "words": [
            "cat",
            "computer",
            "apple"
        ],
        "related words": [
            "feline",
            "programmer",
            "iphone"
        ],
        "password": "f31INEprOgrAmm3r|Ph.NE"
    }
]
```

## Requirements
* Python 3.9.1+

## Acknowledgements
API: https://www.datamuse.com/api/

## Contributions
Contributions are always welcome!  
Just make a [pull request](../../pulls).

## Licence
MIT license
