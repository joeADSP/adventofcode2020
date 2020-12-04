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
	for _, value := range strValues {
		i, _ := strconv.Atoi(value)
		for _, value2 := range strValues {
			j, _ := strconv.Atoi(value2)
			for _, value3 := range strValues {
				k, _ := strconv.Atoi(value3)
				if i == j || j == k || i == k {
					continue
				}
				if i + j + k == 2020 {
					fmt.Println(i, j, k, i + j + k, i * j * k)
					return
				}
			}
		}
	}
}