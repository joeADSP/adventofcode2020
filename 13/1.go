package main

import (
	"fmt"
	"io/ioutil"
	// "strconv"
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

func main() {
	// arrival_time := 939
	// bus_times := []int{7,13,59,31,19}

	arrival_time := 1011416
	bus_times := []int{41, 37, 911, 13, 17, 23, 29, 827, 19}

	fmt.Println(arrival_time)
	fmt.Println(bus_times)
	var remainder int
	var wait int
	var wait_store int
	var best int
	wait_store = 1000000
	for _, bus_time := range bus_times {
		remainder = arrival_time % bus_time
		wait = bus_time - remainder
		if wait != 0 && wait < wait_store {
			best = bus_time
			wait_store = wait
		}
	}
	answer := best * wait_store
	fmt.Println(answer)
}
