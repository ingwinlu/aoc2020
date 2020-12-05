use std::fs::File;
use std::io::{self, BufRead};

#[derive(Debug)]
struct Entry {
    fst: usize,
    snd: usize,
    letter: char,
    candidate: String,
}

impl Entry {
    fn from_line(str: String) -> Entry {
        // 9-17 v: vvvzvvvvqvvxvvzvpv
        let mut segments = str.split(' ');
        let mut range = segments.next().unwrap().split('-');

        let fst: usize = range.next().unwrap().parse().unwrap();
        let snd: usize = range.next().unwrap().parse().unwrap();

        let letter = segments.next().unwrap().chars().nth(0).unwrap();
        let candidate = segments.next().unwrap().to_string();
        Entry {
            fst,
            snd,
            letter,
            candidate,
        }
    }
}

fn filter1(entry: &Entry) -> bool {
    let counter = entry
        .candidate
        .chars()
        .filter(|char| *char == entry.letter)
        .count();
    (entry.fst..=entry.snd).contains(&counter)
}

fn task1() -> usize {
    let file = File::open("./input.txt").expect("file open failed");
    let raw_lines = io::BufReader::new(file).lines();

    let entries = raw_lines.map(|line| Entry::from_line(line.unwrap()));

    entries.filter(filter1).count()
}

fn filter2(entry: &Entry) -> bool {
    let min = entry.fst - 1;
    let max = entry.snd - 1;

    if (entry.candidate.chars().nth(min).unwrap() == entry.letter)
        != (entry.candidate.chars().nth(max).unwrap() == entry.letter)
    {
        return true;
    }
    false
}

fn task2() -> usize {
    let file = File::open("./input.txt").expect("file open failed");
    let raw_lines = io::BufReader::new(file).lines();

    let entries = raw_lines.map(|line| Entry::from_line(line.unwrap()));
    entries.filter(filter2).count()
}

fn main() {
    println!("task1 {}", task1());
    println!("task2 {}", task2());
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;
    use easybench::bench;

    #[test]
    fn test_bench_1() {
        println!("task1: {}", bench(|| task1()));
        assert!(false);
    }
    #[test]
    fn test_bench_2() {
        println!("task2: {}", bench(|| task2()));
        assert!(false);
    }
}
