const fs = require("fs");

data = fs.readFileSync("./nameData.json", { encoding: "utf8" });

names = JSON.parse(data);

newNames = [];

nameStartSet = new Set();

finalSortedNameMap = {};

// names.forEach((name) => {
//     charcode = name.name.charCodeAt(0);
//     if (charcode <= 97 && charcode >= 122) {
//         charcode = String.fromCharCode(charCodeAt - 32);
//     }
//     finalSortedNameMap[charcode] = [];
// });
// names.forEach((name) => {
//     charcode = name.name.charCodeAt(0);
//     if (charcode <= 97 && charcode >= 122) {
//         charcode = String.fromCharCode(charCodeAt - 32);
//     }
//     // finalSortedNameMap[charcode].add(name);
//     console.log(typeof finalSortedNameMap[charcode])
// });

//Capitalizing first letter of all names

names.forEach((name) => {
    charcode = name.name.charCodeAt(0);
    newName = name.name.toUpperCase();
    newName = newName.slice(0, 1) + newName.slice(1).toLowerCase();
    // console.log("new Name " + newName);
    newNames.push({ name: newName, sex: name.sex, meaning: name.meaning });
    // console.log(name.name);
});

//set of first letter to add in map

newNames.forEach((name) => {
    charcode = name.name.charCodeAt(0);
    if (charcode <= 97 && charcode >= 122) {
        charcode = charcode - 32;
    }
    nameStartSet.add(String.fromCharCode(charcode));
    // console.log(name.name);
});
////////////////////////
bruh = new Set();
newNames.forEach((name) => {
    bruh.add(name.name[0]);
});
console.log(bruh);
newNames.sort((a, b) => {
    let fa = a.name.toLowerCase(),
        fb = b.name.toLowerCase();

    if (fa < fb) {
        return -1;
    }
    if (fa > fb) {
        return 1;
    }
    return 0;
});
bruh = new Set();
newNames.forEach((name) => {
    bruh.add(name.name[0]);
});
console.log(bruh);
// bruh.forEach((b) => console.log(b));

//adding in map

nameStartSet = Array.from(nameStartSet).sort();
nameStartSet.forEach((charToStartsWith) => {
    finalSortedNameMap[charToStartsWith] = newNames.filter((name) =>
        name.name.startsWith(charToStartsWith)
    );
});

console.log(nameStartSet);
console.log(newNames.length);

fs.writeFileSync("./sortedNames.json", JSON.stringify(newNames));

data = fs.readFileSync("./sortedNames.json", { encoding: "utf8" });

names = JSON.parse(data);
newNames = [];
for (let i = 1; i <= names.length; i++) {
    newName = { id: i, ...names[i] };
    // newName = names[i];
    // newName["id"] = i;
    newNames.push(newName);
}

fs.writeFileSync("./idNames.json", JSON.stringify(newNames));
// fs.writeFileSync("./sortedNames.json", JSON.stringify(finalSortedNameMap));

// for (var i = 0; i < 128; i++){
//     console.log(i+" = "+String.fromCharCode(i))
// }
