package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func loadFile(filename string) []string {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	strValues := strings.Split(strings.Replace(string(data), "\r", "", -1), "\n")
	return strValues
}

func parseInstruction(line string) (string, int) {
	code := line[:3]
	value, _ := strconv.Atoi(line[4:])
	return code, value
}

func getPosAndAccMovements(line string) (int, int) {
	code, value := parseInstruction(line)
	pos_delta, acc_delta := 1, 0
	switch code {
	case "acc":
		acc_delta = value
	case "jmp":
		pos_delta = value
	}
	return pos_delta, acc_delta
}

func contains(slice []int, element int) bool {
	for _, a := range slice {
		if a == element {
			return true
		}
	}
	return false
}

func main() {
	strValues := loadFile("data.txt")
	var history []int
	acc, pos := 0, 0
	for {
		if contains(history, pos) {
			break
		}

		history = append(history, pos)
		line := strValues[pos]
		pos_delta, acc_delta := getPosAndAccMovements(line)
		pos += pos_delta
		acc += acc_delta
	}
	fmt.Println(acc)
}
