package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func LoadFile(filename string) []string {
	data, err := ioutil.ReadFile("data.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.Replace(string(data), "\r", "", -1), "\n")
	strValues := lines[:len(lines)-1]
	return strValues
}


func StrArrayToInt(array []string) []int {
	var output = []int{}
	for _, item := range array {
		x, err := strconv.Atoi(item)
		if err != nil {
			panic(err)
		}
		output = append(output, x)
	}
	return output
}


func main() {
	strValues := LoadFile("data.txt")
	correct := 0

	for _, line := range strValues{
		password := string(strings.TrimSpace(strings.Split(line, ":")[1]))
		positions := StrArrayToInt(strings.Split(strings.Split(strings.Split(line, ":")[0], " ")[0], "-"))
		character := strings.Split(strings.Split(line, ":")[0], " ")[1]
		
		if bool(string(password[positions[0] - 1]) == character) != bool(string(password[positions[1] - 1]) == character) {
			correct += 1
		}        
	}
	fmt.Println(correct)
}