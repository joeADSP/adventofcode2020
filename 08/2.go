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

func createAmendedDataWithFlippedElements(code string, raw_data []string, target_line_id int) []string {
	data := append([]string(nil), raw_data...)
	if code == "nop" {
		data[target_line_id] = strings.Replace(data[target_line_id], "nop", "jmp", -1)
	}
	if code == "jmp" {
		data[target_line_id] = strings.Replace(data[target_line_id], "jmp", "nop", -1)
	}
	return data
}

func main() {
	raw_data := loadFile("data.txt")
	var acc int
	for target_line_id, change_line := range raw_data {
		code, _ := parseInstruction(change_line)
		if code == "acc" {
			continue
		}
		data := createAmendedDataWithFlippedElements(code, raw_data, target_line_id)

		var history []int
		acc = 0
		pos, exit_properly := 0, false
		for {
			if contains(history, pos) {
				break
			}
			if pos == len(data) {
				exit_properly = true
				break
			}

			history = append(history, pos)
			line := data[pos]
			pos_delta, acc_delta := getPosAndAccMovements(line)
			pos += pos_delta
			acc += acc_delta
		}
		if exit_properly {
			break
		}
	}
	fmt.Println(acc)
}
