fn solve1(ast: u64, bst: u64) -> u64 {
    let af = 16807;
    let bf = 48271;
    let m = 2147483647;

    let mut a = ast;
    let mut b = bst;

    let mut sum = 0;
    for _ in 0..40000000 {
        a = (a * af) % m;
        b = (b * bf) % m;

        if a & 0xffff == b & 0xffff {
            sum += 1;
        }
    }

    sum
}

fn solve2(ast: u64, bst: u64) -> u64 {
    let af = 16807;
    let bf = 48271;
    let m = 2147483647;

    let mut a = ast;
    let mut b = bst;

    let mut sum = 0;
    for _ in 0..5000000 {
        loop {
            a = (a * af) % m;

            if a % 4 == 0 {
                break;
            }
        }
        loop {
            b = (b * bf) % m;

            if b % 8 == 0 {
                break;
            }
        }

        if a & 0xffff == b & 0xffff {
            sum += 1;
        }
    }

    sum
}

fn main() {
    println!("{}", solve1(873, 583));
    println!("{}", solve2(873, 583));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        assert_eq!(solve1(65, 8921), 588);
        assert_eq!(solve2(65, 8921), 309);
    }
}
