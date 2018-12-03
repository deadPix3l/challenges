require 'httparty'
module AdventApi
    def self.get_day(day, year=2018,     session="[redacted]")
        HTTParty.get("https://adventofcode.com/#{year}/day/#{day}/input", cookies: {session: session}).body
    end
end
