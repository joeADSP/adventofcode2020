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

func main() {
	strValues := LoadFile("data.txt")
	correct := 0

	for _, line := range strValues{
		password := strings.TrimSpace(strings.Split(line, ":")[1])
		character := strings.Split(strings.Split(line, ":")[0], " ")[1]
		count := strings.Count(password, character)
		allowed_range := strings.Split(strings.Split(strings.Split(line, ":")[0], " ")[0], "-")
		lower, _ := strconv.Atoi(allowed_range[0])
		upper, _ := strconv.Atoi(allowed_range[1])

		if count >= lower && count <= upper {
			correct += 1
		}
	}
	fmt.Println(correct)
}