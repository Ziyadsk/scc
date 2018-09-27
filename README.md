# scc
A Great cheat sheet and a quick reference command line tool for HTML, CSS and JS .

## Installing
- Download the project and run the install script.
`./install.sh`

## Usage
```shell
scc [-h]  [ -html [HTML] | -css [CSS] | -js [JS] ] | [-rand {html,css,js}]
```
## Examples
```shell
scc -js array.map
```
![map](https://github.com/Ziyadsk/scc/blob/master/screenshots/map.png)

### Check for available propreties/methods 
```shell
scc -css
```
(image cropped to fit screen)
![available](https://github.com/Ziyadsk/scc/blob/master/screenshots/available.png)

### Get random proprety/method

#### CSS example

```shell
scc -rand css 
``` 

![randomcss](https://github.com/Ziyadsk/scc/blob/master/screenshots/randomcss.png)

#### JS example
```shell
scc -rand js 
``` 

![randomjs](https://github.com/Ziyadsk/scc/blob/master/screenshots/randomjs.png)
 
