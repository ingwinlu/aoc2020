use std::collections::HashMap;
use std::fs;

extern crate pest;
#[macro_use]
extern crate pest_derive;
use pest::Parser;

#[derive(Parser)]
#[grammar = "passports.pest"]
struct PassportsParser;

#[derive(Debug)]
struct Passport {
/*
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
*/
    byr: String,
    iyr: String,
    eyr: String,
    hgt: String,
    hcl: String,
    ecl: String,
    pid: String,
    cid: Option<String>
}

impl Passport {
    fn from_hashmap(map: HashMap<&str, &str>) -> Option<Passport> {
        let byr = match map.get("byr") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let iyr = match map.get("iyr") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let eyr = match map.get("eyr") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let hgt = match map.get("hgt") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let hcl = match map.get("hcl") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let ecl = match map.get("ecl") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        let pid = match map.get("pid") {
            Some(val) => {val}
            None => {return None}
        }.to_string();
        Some(Passport{
            byr,
            iyr,
            eyr,
            hgt,
            hcl,
            ecl,
            pid,
            cid: map.get("cid").map(|cid|cid.to_string())
        })
    }
}


fn task1() -> u32 {
    let unparsed_file = fs::read_to_string("./input.txt").expect("cannot read file");
    let passports = PassportsParser::parse(Rule::passports, &unparsed_file).unwrap().next().unwrap();

    let mut valid = 0u32;

    for passport in passports.into_inner() {
        if let Rule::passport = passport.as_rule() {
            let mut hashmap = HashMap::new();
            for pair in passport.into_inner() {
                if let Rule::pair = pair.as_rule() {
                    let mut inner = pair.into_inner();
                    let key = inner.next().unwrap().as_str();
                    let value = inner.next().unwrap().as_str();
                    hashmap.insert(key, value);
                }
            }
            if Passport::from_hashmap(hashmap).is_some() {
                valid += 1;

            }
        }
    }
    valid
}

fn task2() -> u32 {
    0
}

fn main() {
    println!("{}", task1());
    println!("{}", task2());
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;
    use easybench::bench;

    #[test]
    fn test_bench_1() {
        println!("task1: {}", bench(|| task1()));
    }
    #[test]
    fn test_bench_2() {
        println!("task2: {}", bench(|| task2()));
    }
}
