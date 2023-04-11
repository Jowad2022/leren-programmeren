function bereken_poten(giraffen,zebras,struisvogels){
    alle_poten = 0
    alle_poten = giraffen * 4 + alle_poten
    alle_poten = zebras * 4 + alle_poten
    alle_poten = struisvogels * 2 + alle_poten
    return alle_poten
}
vraag1 = Number(prompt("hoeveel giraffen zie je?: "))

vraag2= Number(prompt("hoeveel struisvogels zie je?: "))

vraag3 = Number(prompt("hoeveel zebras zie je?: "))

alert(bereken_poten(vraag1,vraag3,vraag2))

