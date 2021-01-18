// This is still time limit exceeded
package main

import "fmt"

func main() {
	var c int
	fmt.Scanf("%d", &c)

	txt := "A"
	for i := 0; i < c; i++ {
		new_txt := ""
		for _, c := range txt {
			if c == 'A' {
				new_txt += "B"
			} else {
				new_txt += "BA"
			}
		}
		txt = new_txt
	}
	ct := []int{0, 0}
	for _, c := range txt {
		if c == 'A' {
			ct[0] += 1
		} else {
			ct[1] += 1
		}
	}
	fmt.Printf("%d %d\n", ct[0], ct[1])
}
