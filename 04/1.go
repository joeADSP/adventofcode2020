package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func loadFile(filename string) []string {
	data, err := ioutil.ReadFile("data.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(strings.Replace(string(data), "\r", "", -1), "\n\n")
	strValues := lines[:len(lines)-1]
	return strValues
}

func main() {
	strValues := loadFile("data.txt")
	targets := []string{"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}

	count := 0
outer:
	for _, item := range strValues {
		for _, target := range targets {
			if !strings.Contains(item, target) {
				continue outer
			}
		}
		count += 1
	}
	fmt.Println(count)
}
