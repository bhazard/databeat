package main

import (
	"os"

	"github.com/elastic/beats/libbeat/beat"

	"github.com/bhazard/databeat/beater"
)

func main() {
	err := beat.Run("databeat", "", beater.New)
	if err != nil {
		os.Exit(1)
	}
}
