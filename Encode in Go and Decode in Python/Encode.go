package main

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"fmt"
	"os"
)

// encrypt in golang and created public and private key
func encryptString(s string) string {
	publicKey, _ := os.ReadFile("keys/public.pem")
	block, _ := pem.Decode([]byte(publicKey))
	fmt.Println(block)
	if block.Type != "RSA PUBLIC KEY" {
		fmt.Println("error decoding public key from pem")
	}
	parsedKey, err := x509.ParsePKCS1PublicKey(block.Bytes)
	if err != nil {
		fmt.Println("error parsing key")
	}
	rng := rand.Reader
	ciphertext, err := rsa.EncryptOAEP(sha256.New(), rng, parsedKey, []byte(s), nil)
	if err != nil {
		fmt.Println("err")
	}
	return base64.StdEncoding.EncodeToString(ciphertext)
}
func main() {
	s := "This is Datazip Call"
	fmt.Println("Here is encrypted text : ", encryptString(s))
}
