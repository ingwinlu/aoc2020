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
    byr: String,
    iyr: String,
    eyr: String,
    hgt: String,
    hcl: String,
    ecl: String,
    pid: String,
    cid: Option<String>,
}

impl Passport {
    fn from_hashmap(map: HashMap<&str, &str>) -> Option<Passport> {
        let byr = match map.get("byr") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let iyr = match map.get("iyr") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let eyr = match map.get("eyr") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let hgt = match map.get("hgt") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let hcl = match map.get("hcl") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let ecl = match map.get("ecl") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let pid = match map.get("pid") {
            Some(val) => val,
            None => return None,
        }
        .to_string();
        let cid = map.get("cid").map(|cid| cid.to_string());
        Some(Passport {
            byr,
            iyr,
            eyr,
            hgt,
            hcl,
            ecl,
            pid,
            cid,
        })
    }

    fn validate(&self) -> bool {
        fn validate_hgt(hgt: &str) -> bool {
            let l = hgt.len();
            match &hgt[l - 2..] {
                "cm" => hgt[..(l - 2)]
                    .parse::<u32>()
                    .map_or(false, |i| i >= 150 && i <= 193),
                "in" => hgt[..(l - 2)]
                    .parse::<u32>()
                    .map_or(false, |i| i >= 59 && i <= 76),
                _ => false,
            }
        }
        fn validate_ecl(ecl: &String) -> bool {
            match &ecl[..] {
                "amb" => true,
                "blu" => true,
                "brn" => true,
                "gry" => true,
                "grn" => true,
                "hzl" => true,
                "oth" => true,
                _ => false
            }
        }
        self.byr
            .parse::<u32>()
            .map(|byr| byr >= 1920 && byr <= 2002)
            .unwrap_or(false)
            && self
                .iyr
                .parse::<u32>()
                .map(|iyr| iyr >= 2010 && iyr <= 2020)
                .unwrap_or(false)
            && self
                .eyr
                .parse::<u32>()
                .map(|eyr| eyr >= 2020 && eyr <= 2030)
                .unwrap_or(false)
            && validate_hgt(&self.hgt)
            && self.hcl.starts_with('#')
            && self.hcl.len() == 7
            && self.hcl[1..]
                .chars()
                .all(|c| "0123456789abcdef".contains(c))
            && validate_ecl(&self.ecl)
            && self.pid.len() == 9
            && self.pid.chars().all(|c| c.is_numeric())
    }
}

fn parse_passports() -> Vec<Passport> {
    let unparsed_file = fs::read_to_string("./input.txt").expect("cannot read file");
    let passports = PassportsParser::parse(Rule::passports, &unparsed_file)
        .unwrap()
        .next()
        .unwrap();

    let mut passport_vec = Vec::new();

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
            if let Some(pp) = Passport::from_hashmap(hashmap) {
                passport_vec.push(pp);
            }
        }
    }
    passport_vec
}

fn task1() -> usize {
    let passports = parse_passports();
    passports.len()
}

fn task2() -> usize {
    let passports = parse_passports();
    let valid: Vec<Passport> = passports.into_iter().filter(|pp| pp.validate()).collect();
    valid.len()
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
        panic!();
    }
    #[test]
    fn test_bench_2() {
        println!("task2: {}", bench(|| task2()));
        panic!();
    }
}
